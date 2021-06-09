import projectsActions from "../api/projectsActions";


export function useProjects() {
    const createProject = async (data) => {
        return await projectsActions.createProject(data);
    }

    return {
        createProject
    }
}