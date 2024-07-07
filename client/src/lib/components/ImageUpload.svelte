<script lang="ts">
  import { FileDropzone } from "@skeletonlabs/skeleton";
  import MdiLightCloudUpload from "~icons/mdi-light/cloud-upload";
  import SvgSpinners3DotsMove from "~icons/svg-spinners/3-dots-move";
  import { Button } from "$lib/components/ui/button";
  import { goto } from "$app/navigation";
  import { fade } from "svelte/transition";
  import { serverUrl } from "$lib/config.js";

  let files: FileList;
  let errorMessage = "";
  let isError = false;
  let isUploading = false;
  let imgSrc = "";
  $: showImage = imgSrc !== "";

  function onChangeHandler(e: Event): void {
    const target = e.target as HTMLInputElement;
    if (target.files && target.files.length > 0) {
      const file = target.files[0];
      const reader = new FileReader();
      reader.onload = () => {
        imgSrc = reader.result as string;
      };
      reader.readAsDataURL(file);
    }
  }

  function clearImage(): void {
    isError = false;
    imgSrc = "";
  }

  function scrollToUpload(elementId: string) {
    const elementToScrollTo = document.getElementById(elementId);

    if (!elementToScrollTo) {
      console.warn(`Element with ID '${elementId}' not found.`);
      return;
    }

    elementToScrollTo.scrollIntoView({ behavior: "smooth" });
  }

  async function submitImage(): Promise<void> {
    if (!files) {
      handleError("No image to submit");
      return;
    }
    scrollToUpload("upload-image");

    try {
      isError = false;
      isUploading = true;

      const formData = new FormData();
      formData.append("image", files[0]);

      const response = await fetch(`${serverUrl}/image`, {
        method: "POST",
        body: formData,
      });

      if (!response.ok) {
        const errorData = await response.json();
        console.error(errorData.error);
        handleError(errorData.error);
        return;
      }

      const data = await response.json();
      if (data && data.cropped_image && data.analysis) {
        localStorage.setItem("croppedImage", data.cropped_image);
        localStorage.setItem("analysis", JSON.stringify(data.analysis));
        goto(`/analysis`);
      } else {
        throw new Error("Received incomplete data from server");
      }
    } catch (error) {
      handleError(
        "Failed to process the image. Please try another photo or try again later.",
      );
    } finally {
      isUploading = false;
    }
  }

  function handleError(message: string): void {
    isError = true;
    errorMessage = message;
  }
</script>

{#if showImage}
  <div
    class="flex h-fit max-w-sm flex-col items-center justify-center rounded-xl border bg-primary-foreground p-4"
    id="upload-image"
  >
    <img
      src={imgSrc}
      alt="Preview"
      class="w-full rounded-lg transition-opacity duration-300"
      class:opacity-50={isUploading}
      in:fade
    />
    <div class="mt-4 flex items-center space-x-4" in:fade>
      <Button on:click={submitImage} disabled={isUploading}>Submit</Button>
      <Button on:click={clearImage} variant="outline" disabled={isUploading}
        >Clear</Button
      >
    </div>
    {#if isError || isUploading}
      <div
        class="mt-4 text-sm"
        class:text-destructive={isError}
        class:text-muted-foreground={isUploading}
        in:fade
      >
        {#if isError}
          {errorMessage}
        {:else}
          <SvgSpinners3DotsMove />
        {/if}
      </div>
    {/if}
  </div>
{:else}
  <div
    role="none"
    id="upload-image"
    class=" flex aspect-square max-w-md flex-col items-center justify-center rounded-xl border bg-primary-foreground text-base text-muted-foreground transition duration-200 hover:bg-background"
  >
    <MdiLightCloudUpload class="text-4xl" />
    <FileDropzone
      name="files"
      class="border-none"
      type="file"
      bind:files
      on:change={onChangeHandler}
    >
      <svelte:fragment slot="message">
        Click to upload a photo or drag and drop it here.
      </svelte:fragment>
      <svelte:fragment slot="meta"
        >Allowed formats: PNG and JPG.</svelte:fragment
      >
    </FileDropzone>
  </div>
{/if}
