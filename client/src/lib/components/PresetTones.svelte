<script lang="ts">
  import { OnMount } from "fractils";
  import Swatch from "./Swatch.svelte";

  let preset_tones = [
    "#f5ddc8",
    "#ecd8a2",
    "#e1b77e",
    "#c48a58",
    "#825e45",
    "#56412d",

    "#f4d1c8",
    "#ecc7a2",
    "#e1a67d",
    "#c47858",
    "#825245",
    "#56352c",

    "#e9d1d1",
    "#dcc7ae",
    "#caa18a",
    "#b47864",
    "#75524e",
    "#4a3435",
  ];
  // preset_tones = shuffle(preset_tones);

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
