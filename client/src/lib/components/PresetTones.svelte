<script lang="ts">
  import { OnMount } from "fractils";
  import Swatch from "./Swatch.svelte";

  let preset_tones = [
    "#fde7ad",
    "#d49e7a",
    "#cf9660",
    "#b36644",
    "#ffe3c3",
    "#edc091",
    "#ad8b60",
    "#7f4522",
    "#f2c380",
    "#936036",
    "#5e310f",
    "#291609",
  ];
  preset_tones = shuffle(preset_tones);

  function shuffle(array: string[]) {
    let currentIndex = array.length,
      randomIndex;

    while (currentIndex != 0) {
      randomIndex = Math.floor(Math.random() * currentIndex);
      currentIndex--;
      [array[currentIndex], array[randomIndex]] = [
        array[randomIndex],
        array[currentIndex],
      ];
    }

    return array;
  }
</script>

<div
  class="my-8 grid w-full max-w-6xl grid-cols-4 gap-2 px-8 md:my-12 md:grid-cols-6 md:gap-4 md:px-24"
  id="color-slide"
>
  {#each preset_tones as color, index}
    <OnMount>
      <a href={`/analysis/${color.replace(/^#/, "")}`}>
        <Swatch {color} duration={index * 200} translateY={50} label={null} />
      </a>
    </OnMount>
  {/each}
</div>
