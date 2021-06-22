import {ref} from 'vue'
import profileActions from "../api/profileActions";


const profile = ref({})

export function useProfile() {

    const getProfile = async () => {
        return await profileActions.getProfile()
            .then(r => {
                profile.value = r;
                return r;
            })
    }
    const searchProfiles = async (str) => {
        return await profileActions.searchProfiles(str);
    }

    return {
        getProfile,
        profile,
        searchProfiles
    }
}