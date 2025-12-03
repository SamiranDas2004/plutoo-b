import { onMounted } from 'vue'
import { updateMetaTags } from '../utils/seo'

export function useSeo(meta) {
  onMounted(() => {
    updateMetaTags(meta)
  })
}
