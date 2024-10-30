import axios from "axios";
export default {
  state: {
    shopItems: [],
  },
  mutations: {
    setShopItems(state, items) {
      // 创建一个新的 Map 来存储合并后的元素
      const map = new Map();

      // 遍历第一个列表，将每个对象放入 Map 中
      items.forEach((item) => {
        map.set(item.id, { ...item });
      });
      console.log("set:");
      console.log(items);

      // 遍历第二个列表
      state.shopItems.forEach((item) => {
        // 如果 Map 中已经存在相同 id 的元素，则合并 quantity
        if (map.has(item.id)) {
          const existingItem = map.get(item.id);
          existingItem.quantity += item.quantity;
          map.set(item.id, existingItem);
        } else {
          // 否则直接添加到 Map 中
          map.set(item.id, { ...item });
        }
      });
      state.shopItems = Array.from(map.values());
      console.log("merge:");
      console.log(state.shopItems);
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
