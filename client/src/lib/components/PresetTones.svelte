<script lang="ts">
  import { OnMount } from "fractils";
  import Swatch from "./Swatch.svelte";
  import { PRESET_TONES } from "$lib/constants";
</script>

<div
  class="my-8 grid w-full max-w-6xl grid-cols-4 gap-2 px-8 md:my-12 md:grid-cols-6 md:gap-4 md:px-24"
  id="color-slide"
>
  {#each PRESET_TONES as color, index}
    <OnMount>
      <a href={`/analysis/preset/${color.replace(/^#/, "")}`}>
        <Swatch {color} duration={index * 200} translateY={50} label={null} />
      </a>
    </OnMount>
  {/each}
</div>
