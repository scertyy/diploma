<template>
    <button class="base-button">
        <slot></slot>
    </button>
</template>

<style lang="scss">
    .base-button {
        font-style: normal;
        font-weight: bold;
        font-size: 20px;
        line-height: 25px;
        text-align: center;

        background: #FFD15C;
        border: 2px solid #FFD15C;
        border-radius: 8px 4px;

        color: #252525;
        padding: 20px 64px;
        cursor: pointer;

        &.base-button_w-100 {
            width: 100%;
        }

        &.base-button_small {
            font-style: normal;
            font-weight: bold;
            font-size: 18px;
            line-height: 23px;
            padding: 9px 38px;
        }
        &.base-button_cancel {
            background: #303030;
            color: #FFFFFF;
        }
    }
</style>