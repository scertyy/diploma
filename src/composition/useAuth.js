import authActions from "../api/authActions";

export function useAuth() {
    const tryAuth = async (data) => {
        return await authActions.tryAuth(data);
    }
    const tryReg = async (data) => {
        return await authActions.tryReg(data);
    }


    return {
        tryAuth,
        tryReg
    }

}