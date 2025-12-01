'use client';

import { useEffect, useState } from 'react';
import { useRouter } from 'next/navigation';
import { Users, MessageSquare, FileText, TrendingUp } from 'lucide-react';
import { AnalyticsCard } from '@/components/analytics-card';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { analyticsAPI } from '@/lib/api';
import axios from 'axios';

const API_BASE = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

interface ChartData {
  date: string;
  visitors: number;
  messages: number;
}

interface DashboardStats {
  visitorsToday: number;
  messagesToday: number;
  totalMessages: number;
  totalSessions: number;
  documentsCount: number;
  chartData: ChartData[];
}

export default function DashboardPage() {
  const router = useRouter();
  const [stats, setStats] = useState<DashboardStats>({
    visitorsToday: 0,
    messagesToday: 0,
    totalMessages: 0,
    totalSessions: 0,
    documentsCount: 0,
    chartData: [],
  });
  const [loading, setLoading] = useState(true);
  const [period, setPeriod] = useState<7 | 30>(7);

  useEffect(() => {
    fetchStats();
  }, [period]);

  const fetchStats = async () => {
    try {
      const token = localStorage.getItem('authToken');
      const response = await axios.get(`${API_BASE}/analytics/dashboard?days=${period}`, {
        headers: { Authorization: `Bearer ${token}` },
      });
      setStats(response.data);
    } catch (error) {
      console.error('Failed to fetch analytics:', error);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return <div className="text-center py-12">Loading...</div>;
  }

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-3xl font-bold text-slate-900">Dashboard</h1>
        <p className="text-slate-600 mt-1">Welcome back! Here's your platform overview.</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        <AnalyticsCard
          title="Visitors Today"
          value={stats.visitorsToday}
          icon={Users}
          trend={{ value: 12, isPositive: true }}
          onClick={() => router.push('/dashboard/visitors')}
        />
        <AnalyticsCard
          title="Messages Today"
          value={stats.messagesToday}
          icon={MessageSquare}
          trend={{ value: 15, isPositive: true }}
          onClick={() => router.push('/dashboard/sessions')}
        />
        <AnalyticsCard
          title="Total Messages"
          value={stats.totalMessages}
          icon={MessageSquare}
          onClick={() => router.push('/dashboard/sessions')}
        />
        <AnalyticsCard
          title="Total Visitors"
          value={stats.totalSessions}
          icon={TrendingUp}
          onClick={() => router.push('/dashboard/visitors')}
        />
      </div>

      {/* Chart Section */}
      <Card>
        <CardHeader>
          <div className="flex justify-between items-center">
            <CardTitle>Activity Overview</CardTitle>
            <div className="flex gap-2">
              <Button
                variant={period === 7 ? 'default' : 'outline'}
                size="sm"
                onClick={() => setPeriod(7)}
              >
                7 Days
              </Button>
              <Button
                variant={period === 30 ? 'default' : 'outline'}
                size="sm"
                onClick={() => setPeriod(30)}
              >
                30 Days
              </Button>
            </div>
          </div>
        </CardHeader>
        <CardContent>
          <div className="h-80">
            {stats.chartData.length > 0 ? (
              <div className="flex items-end justify-between h-full gap-2">
                {stats.chartData.map((data, index) => {
                  const maxValue = Math.max(
                    ...stats.chartData.map((d) => Math.max(d.visitors, d.messages))
                  );
                  const visitorHeight = (data.visitors / maxValue) * 100;
                  const messageHeight = (data.messages / maxValue) * 100;

                  return (
                    <div key={index} className="flex-1 flex flex-col items-center gap-2">
                      <div className="w-full flex gap-1 items-end h-64">
                        <div
                          className="flex-1 bg-blue-500 rounded-t hover:bg-blue-600 transition-colors relative group"
                          style={{ height: `${visitorHeight}%` }}
                        >
                          <span className="absolute -top-6 left-1/2 -translate-x-1/2 text-xs font-semibold opacity-0 group-hover:opacity-100">
                            {data.visitors}
                          </span>
                        </div>
                        <div
                          className="flex-1 bg-green-500 rounded-t hover:bg-green-600 transition-colors relative group"
                          style={{ height: `${messageHeight}%` }}
                        >
                          <span className="absolute -top-6 left-1/2 -translate-x-1/2 text-xs font-semibold opacity-0 group-hover:opacity-100">
                            {data.messages}
                          </span>
                        </div>
                      </div>
                      <span className="text-xs text-slate-600">
                        {new Date(data.date).toLocaleDateString('en-US', {
                          month: 'short',
                          day: 'numeric',
                        })}
                      </span>
                    </div>
                  );
                })}
              </div>
            ) : (
              <div className="flex items-center justify-center h-full text-slate-500">
                No data available
              </div>
            )}
          </div>
          <div className="flex justify-center gap-6 mt-4">
            <div className="flex items-center gap-2">
              <div className="w-4 h-4 bg-blue-500 rounded"></div>
              <span className="text-sm text-slate-600">Visitors</span>
            </div>
            <div className="flex items-center gap-2">
              <div className="w-4 h-4 bg-green-500 rounded"></div>
              <span className="text-sm text-slate-600">Messages</span>
            </div>
          </div>
        </CardContent>
      </Card>
    </div>
  );
}
