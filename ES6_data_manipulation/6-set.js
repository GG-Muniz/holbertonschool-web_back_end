export default function setFromArray(array) {
  return new Set(Array.isArray(array) ? array : []);
}
