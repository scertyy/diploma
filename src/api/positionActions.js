import {api} from './api';


export default {
    updatePosition: async (data) => {
        return await api.fetch('PUT', `position/${data.id}/`, data.data, true)
    },
}