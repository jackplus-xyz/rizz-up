declare module "ml5" {
  export function faceApi(
    video: HTMLVideoElement | HTMLImageElement | HTMLCanvasElement,
    options?: object,
  ): Promise<any>;

  export interface FaceApiOptions {
    withLandmarks?: boolean;
    withDescriptors?: boolean;
    minConfidence?: number;
    withTinyNet?: boolean;
  }

  export interface FaceDetectionResult {
    _box: {
      _x: number;
      _y: number;
      _width: number;
      _height: number;
    };
    alignedRect: {
      _box: {
        _x: number;
        _y: number;
        _width: number;
        _height: number;
      };
    };
    parts: {
      mouth: Array<{ _x: number; _y: number }>;
      nose: Array<{ _x: number; _y: number }>;
      leftEye: Array<{ _x: number; _y: number }>;
      rightEye: Array<{ _x: number; _y: number }>;
      rightEyeBrow: Array<{ _x: number; _y: number }>;
      leftEyeBrow: Array<{ _x: number; _y: number }>;
    };
  }

  export function imageClassifier(
    model: string,
    callback?: () => void,
  ): Promise<any>;
  export function soundClassifier(
    model: string,
    options?: object,
    callback?: () => void,
  ): Promise<any>;

  // Add more type definitions as you use more features of ml5
}
