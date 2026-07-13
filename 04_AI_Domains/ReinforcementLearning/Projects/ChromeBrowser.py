import subprocess
import random
import time
import pyautogui

class BrowserEnv:
    def __init__(self):
        self.state = "closed"
    
    def reset(self):
        self.state = "closed"
        return self.state
    
    def step(self, action):
        if action == "open":
            try:
                subprocess.Popen([r"C:\Program Files\Google\Chrome\Application\chrome.exe"])
                time.sleep(2)  # wait for Chrome to open
                pyautogui.hotkey("ctrl", "l")  # focus URL bar
                pyautogui.typewrite("Mozammel Khandakar")
                pyautogui.press("enter")
                self.state = "open"
                reward = 1.0
                done = True
            except Exception as e:
                print("Error opening Chrome:", e)
                reward = -1.0
                done = True
        else:
            reward = -0.1
            done = False
        return self.state, reward, done

class Agent:
    def __init__(self, actions=["open","wait"]):
        self.actions = actions
        self.q_table = {}
        self.lr = 0.1
        self.gamma = 0.9
    
    def choose_action(self, state):
        if random.random() < 0.2:
            return random.choice(self.actions)
        return max(self.actions, key=lambda a: self.q_table.get((state,a),0))
    
    def learn(self, state, action, reward, next_state):
        old_q = self.q_table.get((state,action), 0)
        next_q = max(self.q_table.get((next_state,a),0) for a in self.actions)
        new_q = old_q + self.lr * (reward + self.gamma*next_q - old_q)
        self.q_table[(state,action)] = new_q

# Training loop
env = BrowserEnv()
agent = Agent()

for episode in range(3):
    state = env.reset()
    done = False
    while not done:
        action = agent.choose_action(state)
        next_state, reward, done = env.step(action)
        agent.learn(state, action, reward, next_state)
        state = next_state
        print(f"Episode {episode+1}, Action={action}, State={state}, Reward={reward}")
