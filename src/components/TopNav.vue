<template>
    <div class="top-nav">
        <h1 class="top-nav__title">{{route.meta.header}}</h1>
        <div class="top-nav__input-container">
            <BaseInput class="base-input_searching" placeholder="Поиск"></BaseInput>
            <svg class="top-nav__search-icon" width="28" height="28" viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd" clip-rule="evenodd" d="M13.5465 2.33325C7.35345 2.33325 2.33301 7.24281 2.33301 13.2991C2.33301 19.3553 7.35345 24.2649 13.5465 24.2649C16.1952 24.2649 18.6294 23.3668 20.5481 21.8651L24.1929 25.4202L24.2899 25.5018C24.6283 25.7467 25.108 25.7188 25.4142 25.4186C25.751 25.0884 25.7503 24.5537 25.4126 24.2243L21.8106 20.711C23.6421 18.7593 24.7599 16.1568 24.7599 13.2991C24.7599 7.24281 19.7395 2.33325 13.5465 2.33325ZM13.5461 4.0224C18.7852 4.0224 23.0323 8.17576 23.0323 13.2992C23.0323 18.4226 18.7852 22.576 13.5461 22.576C8.30692 22.576 4.05976 18.4226 4.05976 13.2992C4.05976 8.17576 8.30692 4.0224 13.5461 4.0224Z" fill="#A7A7A7"/>
            </svg>
        </div>
        <div class="top-nav__profile-container">
            <div class="top-nav__notifications-button">
                <svg width="28" height="27" viewBox="0 0 28 27" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path fill-rule="evenodd" clip-rule="evenodd" d="M3.50083 16.7871V16.5681C3.53295 15.9202 3.7406 15.2925 4.10236 14.7496C4.7045 14.0975 5.1167 13.2983 5.29571 12.436C5.29571 11.7695 5.29571 11.0935 5.35393 10.427C5.65469 7.21842 8.82728 5 11.9611 5H12.0387C15.1725 5 18.345 7.21842 18.6555 10.427C18.7137 11.0935 18.6555 11.7695 18.704 12.436C18.8854 13.3003 19.2972 14.1019 19.8974 14.7591C20.2618 15.2972 20.4698 15.9227 20.4989 16.5681V16.7776C20.5206 17.648 20.2208 18.4968 19.6548 19.1674C18.907 19.9515 17.8921 20.4393 16.8024 20.5384C13.607 20.8812 10.383 20.8812 7.18762 20.5384C6.09914 20.435 5.08576 19.9479 4.33521 19.1674C3.778 18.4963 3.48224 17.6526 3.50083 16.7871Z" stroke="#A7A7A7" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                    <path d="M9.55518 23.8518C10.0545 24.4785 10.7876 24.884 11.5925 24.9788C12.3973 25.0735 13.2074 24.8495 13.8435 24.3564C14.0391 24.2106 14.2152 24.041 14.3674 23.8518" stroke="#A7A7A7" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                    <rect x="14" width="14" height="13" rx="5" fill="#E2626A"/>
                    <path d="M19.352 5.17V3.94L20.752 3H21.952V10H20.752V4.24L19.352 5.17Z" fill="white"/>
                </svg>
            </div>
            <BaseCircleIcon :src="image"></BaseCircleIcon>
            <div class="top-nav__name">
                {{name}}
            </div>
            <div class="top-nav__avatar"></div>
        </div>
    </div>
</template>

<script>
    import BaseInput from "./Base/BaseInput";
    import {useRoute} from 'vue-router'
    import {useProfile} from "../composition/useProfile";
    import {computed} from 'vue';
    import BaseCircleIcon from "./Base/BaseCircleIcon";
    export default {
        components: {
            BaseCircleIcon,
            BaseInput
        },
        setup() {
            const route = useRoute();
            const {profile} = useProfile()


            return {
                route,
                name: computed(() => profile.value.first_name? `${profile.value.first_name} ${profile.value.last_name}` : ''),
                image: computed(() => profile.value.image),
                profile,
            }
        }
    }
</script>

<style lang="scss">
    .top-nav {
        width: 100%;
        height: 90px;
        filter: drop-shadow(0px 1px 0px #303030);
        background: #252525;
        padding: 16px 24px;


        display: flex;
        align-items: center;
    }
    .top-nav__title {
        margin: 0;
        text-align: left;

        font-family: PT Root UI;
        font-style: normal;
        font-weight: bold;
        font-size: 36px;
        line-height: 115%;
        /* or 41px */

        color: #FFFFFF;

        width: 300px;
    }
    .top-nav__input-container {
        width: 50%;
        position: relative;
        display: flex;
        align-items: center;
    }
    .top-nav__search-icon {
        position: absolute;
        left: 22px;
    }

    .top-nav__profile-container {
        margin-left: auto;
        display: flex;
        align-items: center;
    }
    .top-nav__name {
        font-family: PT Root UI;
        font-style: normal;
        font-weight: bold;
        font-size: 18px;
        line-height: 115%;
        /* identical to box height, or 21px */


        color: #FFFFFF;
        margin: 0 15px;
    }
</style>