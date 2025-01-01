# Chapter 7

- [**Chapter 7-1: Classic Problems of Synchronization-1**](https://www.youtube.com/watch?v=xg2GrholW0o&list=PLwD0kbgjHKhHaUh1mnJIuwm6otLQW3_UP&index=48)
- [**Chapter 7-1: Classic Problems of Synchronization-2**](https://www.youtube.com/watch?v=qK5Dx8uEeLQ&list=PLwD0kbgjHKhHaUh1mnJIuwm6otLQW3_UP&index=49)
- [**Chapter 7-1: Classic Problems of Synchronization-3**](https://www.youtube.com/watch?v=9wdWRY77dgs&list=PLwD0kbgjHKhHaUh1mnJIuwm6otLQW3_UP&index=50)

<center>🚀🚀🚀<strong><i>Add oil</i></strong> 🚀🚀🚀
</center>

## Bounded Buffer

- 有 **Race condition** 的版本

  ```c
      #define BUFFER_SIZE 10
      typedef struct{
          ...
      } item;
      item  buffer[BUFFER_SIZE]; // in shared memory
      int in = 0; // in shared memory
      int out = 0; // in shared memory
  ```

  - 有一個 buffer 來**包含所有資料**
  - Producer **放**資料進入 Buffer

  ```c
      while(((in + 1) % BUFFER_SIZE) == out);
      // 滿了我就 waiting
      buffer[in] = nextProduced;
      in = (in + 1) % BUFFER_SIZE;
  ```

  - Consumer **從 Buffer 取資料**

  ```c
      while(in == out);
      // 空了我就 waiting
      nextConsumed = buffer[out];
      out = (out + 1) % BUFFER_SIZE;
  ```

  - 使用 **shared memory**
  - <mark><strong>因為有可能同時 (1) 存取 (2) 共享 in/ out 並且更新 buffer</strong></mark>
- 沒有 Race Condition 的版本

  - 三個 semaphores

    - Mutex: 協調存取 buffer
    - Full: 當 buffer 滿的時候 Block
    - Empty: 當 buffer 空的時候 Block
  - Producer

    ```c
        wait(empty);
        // empty的狀態，若為 0 就代表滿了 block
        wait(mutex);
        // mutex 統一保護
        ...
        add nextp to buffer
        ...
        signal(mutex);
        signal(full);
        // full 多一個，更新狀態更滿了
    ```
  - Consumer

    ```c
        wait(full);
        // full 是 0 代表空，滿的狀態為 0
        wait(mutex);
        // mutex 統一保護
        ...
        add nextp to buffer
        ...
        signal(mutex);
        signal(empty);
        // 空的狀態加上一，更空了
    ```

## Readers-Writers Problem

- Readers: 讀資料不寫
- Writers: 可以讀寫資料
- **Objective**:

  - 讓一個 Writer 進來而已
  - 允許很多 Readers 進來讀，不會有 race condition
  -
- **Shared Data**:
- 定義變數


  | variable(s) |     type     | init_val |              description              |
  | :---------: | :----------: | :------: | :------------------------------------: |
  |   dataset   |     any     |   N/A   |                  資料                  |
  |    mutex    | binary mutex |    1    |    synchronize access to read_count    |
  |  rw_mutex  | binary mutex |    1    | synchronize writer to write an dataset |
- **Writer**

  ```c
      wait(rw_mutex);
      ...
      /* writing */
      ...
      signal(rw_mutex);
  ```
- **Readers**

  ```c
      wait(mutex); // protection 1
      read_count++;
      if (read_count == 1) 
          wait(rw_mutex); // first mutex
      signal(mutex); // protection 1

      ... // no need for protection since there's no writing involved
      /* Reading */
      ...

      wait(mutex); // protection 2
      read_count--;
      if (read_count == 0)
          signal(rw_mutex); // last mutex
      signla(mutex); // protection 2
  ```

  - 重點:
    - if a writer 在 CS 且 n readers 在等待
      - 一個 reader blocked 在 rw_mutex
      - 其他 n - 1 readers blocked 在 mutex
    - on signal(rw_mutex) by a writer
      - 可以叫醒 a set of waiting readers 或者 a single waiting writer

## Dining-Philosophers Problem

- Requirements

  - 需要兩個 chopsticks
  - 只有五個 chopsticks
- ***Sol-1: 5 Semaphores***

  - `semaphore chopsticks[5]`;
    ```c
     wait(chopstick[i]);
     wait(chopstick[(i + 1) % 5]);
     ...
     // eat
     ...
     signal(chopstick[i])
     signal(chopstick[(i + 1) % 5]) 
     ...
     // thinking
     ...   
    ```
  - Deadlock:
    - 同時飢餓，同時拿起左手邊的筷子
    - 此時同時要求右手邊的筷子
    - 大家都拿不到 😱
    - `i: wait(i); /* permitted */ i: wait(i + 1); /* blocked */`
- **Deadlock-free solution**

  - **左右兩邊**都 available 就取
  - 使用 monitor
  - **Data Structure**:


    |       name       |                   data                   |                         description                         |
    | :--------------: | :---------------------------------------: | :----------------------------------------------------------: |
    |     state[]     | array[0..4] of (thinking, hungry, eating) |      state[i] 設定為 eating 當兩個neighbors都沒 eating      |
    | condition self[] |         array[0..4] of condition         | 當 philosopher *i* 無法得到 chopsticks，用`self[i]` 來 wait |
  - **Pseudocode**

    ```java
    class monitor DiningPhilosopher{
        init(){
            for(int i = 0; i < 5; i++) state[i] = THINKING;
        }
        void pickup(int i){
            state[i] = HUNGRY;
            test(i);
            if(state[i] != EATING) self[i].wait();
            // if failed to eat, blocked.
        }
        void putdown(int i){
            state[i] = THINKING;
            // finished eating
            test((i + 4) % 5)
            // wake up the person on my left
            test((i + 1) % 5)
            // awake another person on my right.
        }
        void test(int i){
            if((state[(i + 4) % 5] != EATING) && (state[i] == HUNGRY) && (state[(i + 1) % 5] != EATING)){
                // if people on both sides are not eating, start eating. 
                state[i] = EATING;
                self[i].signal();
            }
        }

    }

    ```
    ```java
        dp.pickup();
        /*
         * Eating
         */
        dp.putdown();
    ```
  - **Starvation**
