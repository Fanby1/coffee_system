import axios from 'axios';
import router from '@/router';
import store from '@/store';

function getTokenFromLocalStorage() {
  // 从本地存储中取出 token
  return store.getters.token;
}

async function makePaymentRequest(token, paymentData) {
  const url = 'api/pay'; // 替换为实际的付款请求 URL
  const headers = {
    'Authorization': `Bearer ${token}`,
    'Content-Type': 'application/json'
  };

  try {
    const response = await axios.post(url, paymentData, { headers });
    return response;
  } catch (error) {
    console.error('Payment request failed:', error);
    throw error;
  }
}

async function pay(amount, currency, description) {
  const token = getTokenFromLocalStorage();
  console.log("Token: ", token);
  if (!token) {
    console.error('No token found in local storage');
	router.push('/log-in');
    return;
  }

  const paymentData = {
    amount: amount, // 替换为实际的付款金额
    currency: currency, // 替换为实际的货币
    description: description, // 替换为实际的付款描述
	detail: store.getters.cartItems
  };

  try {
    const response = await makePaymentRequest(token, paymentData);
    if (response.status === 200) {
      console.log('Payment successful:', response.data);
    } else {
      console.error('Payment failed:', response.status, response.data);
    }
  } catch (error) {
    console.error('Payment request encountered an error:', error);
  }
}

export {pay};