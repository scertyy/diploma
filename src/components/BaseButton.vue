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
        border-radius: 8px 4px;

        color: #252525;
        padding: 20px 64px;
    }
</style>