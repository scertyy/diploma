import {api} from './api';

export default {
    tryAuth: async (data) => {
        return await api.fetch('POST', 'token/', data)
    },
    tryReg: async (data) => {
        return await api.fetch('POST', 'register/', data)
    },
}