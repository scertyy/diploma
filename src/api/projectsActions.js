import {api} from './api';


export default {
    createProject: async (data) => {
        return await api.fetch('POST', 'project/', data, true)
    },
}