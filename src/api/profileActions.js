import {api} from './api';


export default {
    getProfile: async () => {
        return await api.fetch('GET', 'profile/get_current_profile/', null, true)
    },

    searchProfiles: async (string) => {
        return await api.fetch('GET', `profile/?search=${string}`, null, true)
    },


    editProfile: async (data) => {
        return await api.fetch('POST', 'register/', data)
    },
}