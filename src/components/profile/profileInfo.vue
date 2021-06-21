<template>
    <div class="profile-info">
        <div class="profile-info__row profile-info__row_jst-bw profile-info__row_alg-start profile-info__row_mb-20">
            <div class="profile-info__main-block">
                <div class="profile-info__row">
                    <BaseCircleIcon
                            :src="profile.avatar"
                            class="base-circle-icon_big base-circle-icon_mr-20"
                    ></BaseCircleIcon>
                    <div class="profile-info__info-cont">
                        <div class="profile-info__name">
                            {{profile.username}}
                        </div>
                        <div class="profile-info__sub-name">
                            {{profile.last_name}} {{profile.first_name}}
                        </div>
                        <div class="profile-info__name profile-info__name_mt-20">
                            Уровень {{profile.level}}
                        </div>
                        <div class="profile-info__sub-name">
                            Опыт {{profile.experience}}/{{profile.experience_in_level}}
                        </div>
                    </div>
                </div>
            </div>
            <div class="profile-info__main-block">
                <div class="profile-info__name profile-info__name_alg-slf-end">
                    Мои команды
                </div>
                <div class="profile-info__team-cont">
                    <template  v-for="(team, index) in teams" >
                        <div class="profile-info__sub-name profile-info__sub-name_m-3" :key="team.id" v-if="!team.is_self">
                            {{index+1}}. {{team.name}}
                        </div>
                    </template>

                </div>

            </div>
        </div>
    </div>
</template>
<script>
    import BaseCircleIcon from "../Base/BaseCircleIcon";
    import {computed} from 'vue';
    export default {
        components: {BaseCircleIcon},
        props: {
            profile: Object,
        },
        setup(props) {

            const teams = computed(() => {
                if (!props.profile.value) return [];
                return props.profile.value.filter(i => !i.is_self)
            })

            return {
                profile: props.profile,
                teams
            }
        }
    }
</script>


<style lang="scss">
    .profile-info{
        width: 100%;
        color: white;
    }
    .profile-info__row {
        display: flex;
        align-items: center;
        width: 100%;
        &.profile-info__row_jst-bw {
            justify-content: space-between;
        }
        &.profile-info__row_alg-start {
            align-items: flex-start;
        }
        &.profile-info__row_mb-20 {
            margin-bottom: 20px;
        }
    }
    .profile-info__info-cont {
        display: flex;
        flex-direction: column;
        align-items: flex-start;

        align-self: flex-start;
    }
    .profile-info__main-block {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        flex-shrink: 0;
        max-width: 50%;
    }

    .profile-info__name {
        font-style: normal;
        font-weight: bold;
        font-size: 24px;
        line-height: 115%;
        color: #FFD15C;
        &.profile-info__name_mt-20 {
            margin-top: 20px;
        }
        &.profile-info__name_alg-slf-end {
            align-self: flex-end;
        }
    }
    .profile-info__team-cont {
        width: 100%;
        max-height: 189px;
        overflow: auto;
        margin: 15px 0;
        display: flex;
        flex-direction: column;
        align-items: flex-start;
    }
    .profile-info__sub-name {
        font-style: normal;
        font-weight: bold;
        font-size: 16px;
        line-height: 115%;
        &.profile-info__sub-name_m-3 {
            margin: 3px 0;
        }
    }
</style>
