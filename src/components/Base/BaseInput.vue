<template>
    <input
            :type="type? type: 'text'"
            class="base-input"
            :value="modelValue"
            @input="$emit('update:modelValue', $event.target.value)"
    >
</template>

<script>
    export default {
        props: {
            modelValue: String,


            type: String,
        }
    }
</script>

<style lang="scss">
    .base-input {
        width: 100%;
        background: #303030;
        border-radius: 4.87805px;
        // font-family: PT Root UI;
        font-style: normal;
        font-size: 20px;
        line-height: 25px;

        color: #A7A7A7;
        padding: 22px 24px;
        outline: none;
        &.base-input_mt-30 {
            margin-top: 30px;
        }
        &.base-input_mb-30 {
            margin-bottom: 30px;
        }
        &.base-input_searching {
            padding: 18px 22px 18px 62px;
            font-style: normal;
            font-weight: bold;
            font-size: 18px;
            line-height: 23px;
            color: #A7A7A7;
        }
        &.base-input_modal {
            background: white;
            color: #252525;
            padding: 8px 16px;
        }
    }
</style>
