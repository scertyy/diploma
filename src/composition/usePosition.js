import {} from 'vue'
import positionActions from "../api/positionActions";

export function usePosition() {

    const updatePosition = async (data) => {
        return await positionActions.updatePosition(data)
    }

    return {
        updatePosition
    }
}