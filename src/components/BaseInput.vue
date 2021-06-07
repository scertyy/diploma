<template>
    <input
            class="base-input"
            :value="modelValue"
            @input="$emit('update:modelValue', $event.target.value)"
    >
</template>

<script>
    export default {
        props: {
            modelValue: String,
        }
    }
</script>

<style lang="scss">
    .base-input {
        background: #303030;
        border-radius: 4.87805px;
        font-family: PT Root UI;
        font-style: normal;
        font-weight: bold;
        font-size: 20px;
        line-height: 25px;

        color: #A7A7A7;
        padding: 22px 24px;
        outline: none;
        &.base-input_mb-30 {
            margin-bottom: 30px;
        }
    }
</style>