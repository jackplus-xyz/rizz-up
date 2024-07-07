<script lang="ts">
  import { createEventDispatcher } from "svelte";
  import { writable } from "svelte/store";
  import Swatch from "./Swatch.svelte";

  export let label: string;
  export let color: string;
  const copiedTimeout = writable(0);

  const dispatch = createEventDispatcher();

  function selectColor(color: string) {
    dispatch("colorSelected", { color: color });
    navigator.clipboard
      .writeText(color)
      .then(() => {
        copiedTimeout.set(1000);
      })
      .catch((err) => {
        console.error("Failed to copy color to clipboard:", err);
      });

    window.scrollTo({
      top: 0,
      behavior: "smooth",
    });
  }

  $: copiedTimeout.subscribe((value) => {
    if (value > 0) {
      const timer = setTimeout(() => copiedTimeout.set(value - 1000), 1000);
      return () => clearTimeout(timer);
    }
  });
</script>

<button on:click={() => selectColor(color)} class="w-full">
  <Swatch
    label={$copiedTimeout > 0 ? "Copied!" : label ? label : null}
    {color}
    on:colorSelected
  />
</button>
