<template>
    <div class="index">
        <div class="index__tasks-row">
            <BaseTaskCard class="base-task-card_blue"></BaseTaskCard>
            <BaseTaskCard class="base-task-card_yellow"></BaseTaskCard>
            <BaseTaskCard class="base-task-card_red"></BaseTaskCard>
            <BaseTaskCard class="base-task-card_green"></BaseTaskCard>
        </div>
    </div>
</template>

<script>
    import BaseTaskCard from '../../components/Base/BaseTaskCard';
    import {useProfile} from "../../composition/useProfile";

    import {onMounted} from 'vue';
    export default {
        components: {
            BaseTaskCard
        },
        setup() {

            const {getProfile} = useProfile()

            onMounted(() => {
                getProfile()
            })

            return {}

        }
    }
</script>

<style lang="scss">
    .index {
        width: 100%;
        height: 100%;
        padding: 50px 35px;
    }
    .index__tasks-row {
        width: 100%;
        display: flex;

        justify-content: space-between;
        margin-bottom: 50px;
    }
</style>