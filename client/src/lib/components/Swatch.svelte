<script lang="ts">
  import { cubicOut } from "svelte/easing";
  import { fly, fade } from "svelte/transition";

  export let color: string;
  export let label: string | null | undefined;
  export let duration = 0;
  export let translateY = 0;
  export let translateX = 0;

  function hexToRgb(hex: string): number[] | null {
    const result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
    return result
      ? [
          parseInt(result[1], 16),
          parseInt(result[2], 16),
          parseInt(result[3], 16),
        ]
      : null;
  }
</script>

<div
  class="duration-50 group relative flex aspect-square h-full w-full flex-col items-center justify-between border-muted-foreground transition-all hover:border hover:bg-background hover:p-2 hover:shadow"
  in:fly={{
    x: translateX,
    y: translateY,
    duration: duration,
    easing: cubicOut,
  }}
>
  <div
    class="duration-400 aspect-square w-full rounded-xl border-black transition-all ease-in-out group-hover:h-3/4 group-hover:rounded-none md:rounded-2xl"
    style="background-color: {color};"
  />
  <span
    class="duration-50 my-1 w-full text-left font-mono text-xs font-bold text-primary opacity-0 transition-opacity duration-500 ease-in-out group-hover:opacity-100"
    in:fade
  >
    {hexToRgb(color)}
  </span>
  <span
    class="duration-50 w-full text-left font-mono text-lg font-light text-primary opacity-0 transition-opacity duration-500 ease-in-out group-hover:opacity-100"
    in:fade
  >
    {#if label}
      {label}
    {:else}
      {color.toUpperCase()}
    {/if}
  </span>
</div>
