<template>
    <v-container fluid class="fill-height">
        <v-row class="fill-height">
            <v-col cols="3" class="fill-height">
                <slot name="left"></slot>
            </v-col>
            <v-col cols="9" class="justify-end pa-0">
                <img :src="src" class="fill-height cover-image">
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
export default {
    name: 'AuthenticationLayout',
    props: {
        src: {
            type: String,
            required: true
        }
    }
};
</script>

<style scoped>
.fill-height {
    height: 100%;
}

.cover-image {
    object-fit: cover;
    width: 100%;
}
</style>