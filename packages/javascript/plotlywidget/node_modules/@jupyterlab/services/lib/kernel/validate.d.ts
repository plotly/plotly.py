import { Kernel } from './kernel';
import { KernelMessage } from './messages';
/**
 * Validate a kernel message object.
 */
export declare function validateMessage(msg: KernelMessage.IMessage): void;
/**
 * Validate a `Kernel.IModel` object.
 */
export declare function validateModel(model: Kernel.IModel): void;
/**
 * Validate a server kernelspec model to a client side model.
 */
export declare function validateSpecModel(data: any): Kernel.ISpecModel;
/**
 * Validate a `Kernel.ISpecModels` object.
 */
export declare function validateSpecModels(data: any): Kernel.ISpecModels;
