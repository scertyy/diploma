import {ref} from 'vue';
const routeName = ref('');

export function useRouteName() {

    return {
        routeName,
    }
}