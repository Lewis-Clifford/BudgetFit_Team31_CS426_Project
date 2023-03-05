<template >
<div class="popup-overlay" @click.self="$emit('close')">
<div class="popup-container">
    <div class="popup-content">
<img src="@/assets/240.png" alt="Placeholder image">
  <p>Nutritional values: ...</p>
  <button class="popup-close" @click="$emit('close')">X</button>
  </div>
</div>
</div>

</template>
<script>
export default {
    name: 'PopupComponent'
}
</script>
<style>
    .popup-container {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 9999;
  width: 80%;
  max-width: 600px;
  height: 80%;
  max-height: 600px;
  background-color: white;
  padding: 20px;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5);

}

.popup-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 2;
}

.popup-close {
  position: absolute;
  top: 10px;
  right: 10px;
  font-size: 20px;
  font-weight: bold;
  background-color: transparent;
  border: none;
  cursor: pointer;
  outline: none;
}

.popup-content {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin-top: 25px;
}

.popup-content img {
  max-width: 100%;

}

.popup-content p {
  text-align: center;
  margin-top: 10px;
}

</style>