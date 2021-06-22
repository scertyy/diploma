import {api} from './api';


export default {
    getBoardsFromTeam: async (id) => {
        return await api.fetch('GET', `board/?team=${id}`, null, true)
    },
}