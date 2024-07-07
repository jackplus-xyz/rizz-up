<script lang="ts">
  import { OnMount } from "fractils";
  import SwatchButton from "./SwatchButton.svelte";

  export let colors;
</script>

<div class="grid w-full grid-cols-4 gap-2 md:grid-cols-6">
  {#each colors as color, index}
    <OnMount>
      <SwatchButton
        label={color.name}
        color={color.hex_code}
        duration={250 * index}
        on:colorSelected
      />
    </OnMount>
  {/each}
</div>
