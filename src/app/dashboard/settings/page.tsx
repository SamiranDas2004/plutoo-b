'use client';

import { useEffect, useState } from 'react';
import { Copy, RotateCcw } from 'lucide-react';
import { WidgetSettings } from '@/types';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { ColorPicker } from '@/components/color-picker';
import { CopyButton } from '@/components/copy-button';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs';
import { widgetAPI } from '@/lib/api';
import { useDashboardStore } from '@/store';
import toast from 'react-hot-toast';

export default function SettingsPage() {
  const [loading, setLoading] = useState(true);
  const [settings, setSettings] = useState<WidgetSettings>({
    botToken: '',
    color: '#000000',
    position: 'right',
    welcomeMessage: 'Hello! How can we help?',
  });
  const { widgetSettings, setWidgetSettings } = useDashboardStore();

  useEffect(() => {
    fetchSettings();
  }, []);

  const fetchSettings = async () => {
    try {
      const response = await widgetAPI.get();
      setSettings(response.data);
      setWidgetSettings(response.data);
    } catch (error) {
      toast.error('Failed to load widget settings');
    } finally {
      setLoading(false);
    }
  };

  const handleSave = async () => {
    try {
      await widgetAPI.update(settings);
      setWidgetSettings(settings);
      toast.success('Settings saved');
    } catch (error) {
      toast.error('Failed to save settings');
    }
  };

  const handleRegenerateToken = async () => {
    try {
      const response = await widgetAPI.regenerateToken();
      setSettings({ ...settings, botToken: response.data.botToken });
      toast.success('Token regenerated');
    } catch (error) {
      toast.error('Failed to regenerate token');
    }
  };

  if (loading) {
    return <div className="text-center py-12">Loading...</div>;
  }

  const scriptTag = `<script src="https://cdn.yoursaas.com/widget.js" data-bot-token="${settings.botToken}"></script>`;

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-3xl font-bold text-slate-900">Widget Settings</h1>
        <p className="text-slate-600 mt-1">Configure your chatbot widget.</p>
      </div>

      <Tabs defaultValue="installation" className="space-y-4">
        <TabsList>
          <TabsTrigger value="installation">Installation</TabsTrigger>
          <TabsTrigger value="customization">Customization</TabsTrigger>
        </TabsList>

        <TabsContent value="installation" className="space-y-4">
          <Card>
            <CardHeader>
              <CardTitle className="text-lg">Bot Token</CardTitle>
            </CardHeader>
            <CardContent className="space-y-4">
              <div className="flex gap-2">
                <Input
                  value={settings.botToken}
                  readOnly
                  className="font-mono text-sm"
                />
                <CopyButton text={settings.botToken} label="Copy" />
              </div>
              <Button
                variant="outline"
                onClick={handleRegenerateToken}
                className="gap-2"
              >
                <RotateCcw className="h-4 w-4" />
                Regenerate Token
              </Button>
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle className="text-lg">Installation Script</CardTitle>
            </CardHeader>
            <CardContent className="space-y-4">
              <p className="text-sm text-slate-600">
                Add this script tag to your website to enable the widget:
              </p>
              <div className="bg-slate-900 text-slate-100 p-4 rounded font-mono text-sm overflow-x-auto">
                {scriptTag}
              </div>
              <CopyButton text={scriptTag} label="Copy Script" />
            </CardContent>
          </Card>
        </TabsContent>

        <TabsContent value="customization" className="space-y-4">
          <Card>
            <CardHeader>
              <CardTitle className="text-lg">Appearance</CardTitle>
            </CardHeader>
            <CardContent className="space-y-6">
              <div>
                <label className="text-sm font-medium text-slate-900">Widget Color</label>
                <div className="mt-2">
                  <ColorPicker
                    value={settings.color}
                    onChange={(color) => setSettings({ ...settings, color })}
                  />
                </div>
              </div>

              <div>
                <label className="text-sm font-medium text-slate-900">Position</label>
                <div className="flex gap-4 mt-2">
                  {(['left', 'right'] as const).map((pos) => (
                    <label key={pos} className="flex items-center gap-2 cursor-pointer">
                      <input
                        type="radio"
                        name="position"
                        value={pos}
                        checked={settings.position === pos}
                        onChange={(e) =>
                          setSettings({ ...settings, position: e.target.value as 'left' | 'right' })
                        }
                        className="w-4 h-4"
                      />
                      <span className="text-sm text-slate-700 capitalize">{pos}</span>
                    </label>
                  ))}
                </div>
              </div>

              <div>
                <label className="text-sm font-medium text-slate-900">Welcome Message</label>
                <Input
                  value={settings.welcomeMessage}
                  onChange={(e) =>
                    setSettings({ ...settings, welcomeMessage: e.target.value })
                  }
                  className="mt-2"
                  placeholder="Enter welcome message"
                />
              </div>

              <Button onClick={handleSave} className="w-full">
                Save Changes
              </Button>
            </CardContent>
          </Card>
        </TabsContent>
      </Tabs>
    </div>
  );
}
