<script lang="ts">
  import { OnMount } from "fractils";
  import SwatchButton from "./SwatchButton.svelte";

  export let colors;
</script>

<div class="grid w-full grid-cols-6 gap-1 md:grid-cols-6 md:gap-2">
  {#each colors as color}
    <OnMount>
      <SwatchButton
        label={color.name}
        color={color.hex_code}
        on:colorSelected
      />
    </OnMount>
  {/each}
</div>
