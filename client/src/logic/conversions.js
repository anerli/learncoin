export function hexToFloat(hex) {
  // Convert IEEE hex encoded float as str to float
  let v = new DataView(new ArrayBuffer(4));
  v.setUint32(0, parseInt(hex, 16));
  return v.getFloat32(0);
}

export function floatToHex(f) {
  // Convert IEEE hex encoded float as str to float
  let v = new DataView(new ArrayBuffer(4));
  v.setFloat32(0, f);
  return v.getUint32(0).toString(16);
}