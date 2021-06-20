<template>
    <div class="profile-plans">
        <BaseCircle
                v-for="circle in circles"
                :key="circle.name"
                :percent="circle.percent"
                :cirlce_name="circle.name"
        >
        </BaseCircle>
    </div>
</template>

<script>
    import BaseCircle from '../Base/BaseCircle'
    export default {
        components : {
            BaseCircle
        },
        props: {
            circles: Array,
        },
        setup(props) {

            return {
                circles: props.circles
            }
        }
    }
</script>

<style lang="scss">

    .profile-plans{
        width: 80%;
        margin: 45px auto;
        display: flex;
        justify-content: space-around;
    }
</style>