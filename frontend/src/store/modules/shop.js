import axios from "axios";
export default {
  state: {
    shopItems: [],
  },
  mutations: {
    setShopItems(state, items) {
      state.shopItems = items;
    },
    increaseItemQuantity(state, itemId) {
      const item = state.shopItems.find((item) => item.id === itemId);
      item.quantity++;
    },
    decreaseItemQuantity(state, itemId) {
      const item = state.shopItems.find((item) => item.id === itemId);
      if (item.quantity > 0) {
        item.quantity--;
      }
    },
  },
  actions: {
    async fetchAllItems({ commit }) {
      try {
        const response = await axios.get("/api/coffees");
        const items = response.data.coffees;
        items.forEach((coffee) => {
          coffee.quantity = 0;
        });
        console.log(items);
        commit("setShopItems", items);
      } catch (error) {
        console.error("Error fetching coffee data:", error);
      }
    },
  },
  getters: {
    shopItems(state) {
      return state.shopItems;
    },
    cartItems(state) {
      return state.shopItems.filter((item) => item.quantity > 0);
    },
    totalPrice(state) {
      return state.shopItems.reduce(
        (total, item) => total + item.price * item.quantity,
        0
      );
    },
    cartItemsCount(state) {
      return state.shopItems.reduce((total, item) => total + item.quantity, 0);
    },
    getItemById: (state) => (itemId) => {
      const item = state.shopItems.find((item) => item.id === itemId);
      return item;
    },
    getQuantityById: (state) => (itemId) => {
      const item = state.shopItems.find((item) => item.id === itemId);
      return item.quantity;
    },
  },
};
