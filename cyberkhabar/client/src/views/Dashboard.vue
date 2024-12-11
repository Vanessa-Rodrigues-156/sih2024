<script>
import cybermonitor from '../components/cybermonitor.vue'
import somecomponent from '../components/somecomponent.vue';

export default {
    name: 'DashboardPage',
    components: {
        cybermonitor,
        somecomponent
    }
}
</script>

<template>
    <cybermonitor />  
    <somecomponent />
</template>
