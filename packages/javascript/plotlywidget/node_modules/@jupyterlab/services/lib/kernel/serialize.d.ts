import { KernelMessage } from './messages';
/**
 * Deserialize and return the unpacked message.
 *
 * #### Notes
 * Handles JSON blob strings and binary messages.
 */
export declare function deserialize(data: ArrayBuffer | string): KernelMessage.IMessage;
/**
 * Serialize a kernel message for transport.
 *
 * #### Notes
 * If there is binary content, an `ArrayBuffer` is returned,
 * otherwise the message is converted to a JSON string.
 */
export declare function serialize(msg: KernelMessage.IMessage): string | ArrayBuffer;
