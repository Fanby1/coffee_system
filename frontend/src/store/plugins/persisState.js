export const persistState = (store) => {
  // 当 store 初始化时，从 localStorage 恢复状态
  const savedState = localStorage.getItem("vuexState");
  console.log(savedState);
  if (savedState) {
    store.replaceState(JSON.parse(savedState));
  }
  console.log(store.state);

  // 每当状态变化时，将状态保存在 localStorage 中
  store.subscribe((mutation, state) => {
    localStorage.setItem("vuexState", JSON.stringify(state));
  });
};
