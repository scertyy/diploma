<template>
    <div class="modal-search-profiles" @mousedown.self="close">
        <div class="modal-search-profiles__body">
            <BaseModalHeader>
                Добавить участника
            </BaseModalHeader>
            <div class="modal-search-profiles__input-container">
                <BaseInput class="base-input_modal" v-model="name" placeholder="Поиск..."></BaseInput>
            </div>
            <div class="modal-search-profiles__profiles">
                <div class="modal-search-profiles__profile" v-for="profile in profiles" :key="profile.id"
                    @click="selectProfile(profile.id)"
                     :class="{'modal-search-profiles__profile_active': selectedProfile === profile.id}"
                >
                    <BaseCircleIcon :src="profile.image"></BaseCircleIcon>
                    <div class="modal-search-profiles__user-cont">
                        <div class="modal-search-profiles__name">{{profile.first_name}} {{profile.last_name}}</div>
                        <div class="modal-search-profiles__name">{{profile.username}}</div>
                    </div>
                </div>
            </div>

            <div class="modal-search-profiles__buttons">
                <BaseButton
                        class="base-button_small"
                        @click="save"
                >
                    Добавить
                </BaseButton>
                <BaseButton
                        class="base-button_small base-button_cancel"
                        @click.self="close"
                >
                    Отмена
                </BaseButton>
            </div>
        </div>
    </div>
</template>

<script>
    import BaseButton from '../Base/BaseButton.vue'
    import BaseInput from '../Base/BaseInput.vue'
    import BaseModalHeader from '../Base/BaseModalHeader.vue'

    import {ref, watch} from 'vue';
    import {useProfile} from "../../composition/useProfile";
    import BaseCircleIcon from "../Base/BaseCircleIcon";
    export default {
        components: {BaseCircleIcon, BaseButton, BaseModalHeader, BaseInput },
        setup(props, {emit}) {
            const { searchProfiles } = useProfile()

            const close = () => {
                emit('close')
            }
            const save = () => {
                if (selectedProfile.value) {
                    emit('save', selectedProfile.value);
                }
            }
            const name = ref('');

            let time = new Date().getTime();

            watch(name, (newValue, oldValue) => {
                searchHandler(name.value)
            })
            const profiles = ref([])
            const selectedProfile = ref(null);
            const selectProfile = (id) => {
                selectedProfile.value = id;
            }
            const searchHandler = (value) => {
                let newTime = new Date().getTime();
                time = newTime;
                setTimeout(() => {
                    if (newTime === time) {
                        searchProfiles(name.value)
                            .then(r => {
                                profiles.value = [...r];
                            })
                    }
                }, 500)
            }



            return {
                save,
                close,
                profiles,
                name,

                selectedProfile,
                selectProfile,
            }
        }
    }
</script>

<style lang="scss">
    .modal-search-profiles {
        width: 100vw;
        height: 100vh;
        background: rgba(0, 0, 0, 0.34);
        position: absolute;
        left: 0;
        top: 0;
        z-index: 1300;
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: left;
        &.z-index {
            z-index: 1400;
        }
    }
    .modal-search-profiles__body {
        width: 364px;
        background: #303030;
        border-radius: 9px;
        padding: 20px 0;
        text-align: left;
    }
    .modal-search-profiles__buttons {
        padding: 0 20px;
        width: 100%;
        display: flex;
        justify-content: space-between;
        margin-top: 45px;
    }
    .modal-search-profiles__input-container {
        margin-top: 30px;
        padding: 0 20px;
    }
    .modal-search-profiles__profiles {
        width: 100%;
        margin: 15px 0;
    }
    .modal-search-profiles__profile {
        display: flex;
        align-items: center;
        margin-bottom: 4px;
        position: relative;
        padding: 5px 20px;
        cursor: pointer;
        transition: .2s ease;
        height: 80px;
        &:hover {
            background: #252525;
        }
        &.modal-search-profiles__profile_active {
            background: #252525;
        }
    }
    .modal-search-profiles__user-cont {
        width: 100%;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        height: 60px;
        margin: auto 0 auto 15px;
    }
    .modal-search-profiles__name {
        font-family: PT Root UI;
        font-style: normal;
        font-weight: normal;
        font-size: 22px;
        line-height: 115%;
        /* or 18px */

        display: flex;
        align-items: center;
        color: #FFFFFF;
        &:last-of-type {
            color: #757575;
            font-size: 18px;
        }
    }
</style>