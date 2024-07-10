<script lang="ts">
  import { FileDropzone } from "@skeletonlabs/skeleton";
  import MdiLightCloudUpload from "~icons/mdi-light/cloud-upload";
  import SvgSpinners3DotsMove from "~icons/svg-spinners/3-dots-move";
  import { Button } from "$lib/components/ui/button";
  import { goto } from "$app/navigation";
  import { fade } from "svelte/transition";
  import { onDestroy } from "svelte";

  let files: FileList;
  let errorMessage = "";
  let isError = false;
  let isUploading = false;
  let imgSrc = "";
  $: showImage = imgSrc !== "";

  let loadingMessages = [
    "Uploading image",
    "Coaxing pixels through tubes",
    "Negotiating with firewalls",
    "First-class ticket to servers",
    "Waking face recognition hamsters",
    "Face or potato? Calibrating...",
    "Convincing cats they're faces",
    "Almost there",
  ];
  let currentMessageIndex = 0;
  let messageInterval: ReturnType<typeof setInterval> | undefined;
  let isVisible = true;

  $: currentMessage = loadingMessages[currentMessageIndex];
  let transitionDuration = 10000;

  function updateMessage() {
    isVisible = false;
    setTimeout(() => {
      currentMessageIndex = (currentMessageIndex + 1) % loadingMessages.length;
      isVisible = true;
    }, transitionDuration / 2);
  }

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
      messageInterval = setInterval(updateMessage, transitionDuration);

      const formData = new FormData();
      formData.append("image", files[0]);

      const response = await fetch("api/images/crop", {
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
      if (data.croppedImage) {
        localStorage.setItem("croppedImage", data.croppedImage);
      }

      const localAnalysis = localStorage.getItem("analysis");
      if (localAnalysis) {
        localStorage.removeItem("analysis");
      }

      goto(`/analysis`);
    } catch (error) {
      console.error("Error processing image:", error);
      handleError(
        "Failed to process the image. Please try another photo or try again later.",
      );

      if (messageInterval) {
        clearInterval(messageInterval);
      }
    } finally {
      isUploading = false;

      if (messageInterval) {
        clearInterval(messageInterval);
      }
    }
  }

  onDestroy(() => {
    if (messageInterval) {
      clearInterval(messageInterval);
    }
  });

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
        {:else if currentMessage}
          <div class="flex flex-col items-center gap-1">
            <SvgSpinners3DotsMove />
            {#if isVisible}
              <span transition:fade={{ duration: transitionDuration }}>
                {currentMessage}
              </span>
            {/if}
          </div>
        {/if}
      </div>
    {/if}
  </div>
{:else}
  <div
    role="none"
    id="upload-image"
    class="flex aspect-square max-w-md flex-col items-center justify-center rounded-xl border bg-primary-foreground text-base text-muted-foreground transition duration-200 hover:bg-background"
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
        >Allowed formats: PNG and JPG.
      </svelte:fragment>
    </FileDropzone>
  </div>
{/if}
