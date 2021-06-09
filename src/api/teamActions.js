import {api} from './api';

export default {
    getMyTeams: async (data) => {
        return await api.fetch('GET', 'team/', null, true)
    },
    createTeam: async (data) => {
        return await api.fetch('POST', 'team/', data, true)
    },

    getTeam: async(id) => {
        return await api.fetch('GET', `team/${id}/`, null, true)
    },
    getTeamContributor: async(id) => {
        return await api.fetch('GET', `contributor/?team=${id}`, null, true)
    },
    getTeamProjects: async(id) => {
        return await api.fetch('GET', `project/?team=${id}`, null, true)
    },
    deleteTeam: async(id) => {
        return await api.fetch('DELETE', `team/${id}/`, null, true)
    },
    addContributorToTeam: async(data) => {
        return await api.fetch('POST', `team/add_contributor_to_team/`, data, true)
    },
    deleteContributorFromTeam: async(data) => {
        return await api.fetch('POST', `team/delete_contributor_from_team/`, data, true)
    }

}