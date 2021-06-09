import teamActions from "../api/teamActions";
import {reactive, computed} from 'vue';


const myTeams = reactive({
    data: [],
})

export function useTeam() {
    const getMyTeams = async () => {
        return await teamActions.getMyTeams()
            .then(r => {
                myTeams.data = [...r]
            })
    }
    const createTeam = async (data) => {
        return await teamActions.createTeam(data)
    }
    const deleteTeam = async (id) => {
        return await teamActions.deleteTeam(id);
    }

    const getTeam = async (id) => {
        return await teamActions.getTeam(id);
    }
    const getTeamContributor = async (id) => {
        return await teamActions.getTeamContributor(id);
    }
    const getTeamProjects = async (id) => {
        return await teamActions.getTeamProjects(id);
    }

    const addContributorToTeam = async (data) => {
        return await teamActions.addContributorToTeam(data);
    }
    const deleteContributorFromTeam = async (data) => {
        return await teamActions.deleteContributorFromTeam(data);
    }


    return {
        getMyTeams,
        myTeams: computed(() => myTeams.data),
        createTeam,
        deleteTeam,
        getTeam,
        addContributorToTeam,
        deleteContributorFromTeam,
        getTeamContributor,
        getTeamProjects
    }
}