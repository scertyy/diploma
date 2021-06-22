import boardsActions from "../api/boardsActions";


export function useBoard() {

    const getBoardsFromTeam = async (id) => {
        return await boardsActions.getBoardsFromTeam(id);
    }

    return {
        getBoardsFromTeam,
    }
}