# Perterson's Solution

## 正常的狀況

![1735801721009](images/OS_flowchart_and_procedures_explained/1735801721009.png) 

## 對調 turn 跟 flag[] 的情況

![1735801791530](images/OS_flowchart_and_procedures_explained/1735801791530.png)

# Hardware Solutions

## Disable Interrupts

### 原本 Race Condition 的問題

![1735801862578](images/OS_flowchart_and_procedures_explained/1735801862578.png)

### Disable 來解決

![1735801904151](images/OS_flowchart_and_procedures_explained/1735801904151.png)


## Memory Barriers

### Reorder 的狀況

![1735801967189](images/OS_flowchart_and_procedures_explained/1735801967189.png)


### test_and_set

![1735802012032](images/OS_flowchart_and_procedures_explained/1735802012032.png)

### Lock = false 不用 atomic

![1735802149433](images/OS_flowchart_and_procedures_explained/1735802149433.png)

### Lock and bounded waiting

![1735802216704](images/OS_flowchart_and_procedures_explained/1735802216704.png)

# Liveness

![1735802343484](images/OS_flowchart_and_procedures_explained/1735802343484.png)

# Paging

![1735802444572](images/OS_flowchart_and_procedures_explained/1735802444572.png)


## TLB

![1735802514673](images/OS_flowchart_and_procedures_explained/1735802514673.png)

## read-write bits

![1735802641559](images/OS_flowchart_and_procedures_explained/1735802641559.png)

## Two level paging

![1735802722877](images/OS_flowchart_and_procedures_explained/1735802722877.png)



## Hashed Page Table

![1735802786866](images/OS_flowchart_and_procedures_explained/1735802786866.png)


## IPT

![1735802833782](images/OS_flowchart_and_procedures_explained/1735802833782.png)



## Demand Paging

![1735802896574](images/OS_flowchart_and_procedures_explained/1735802896574.png)

## Copy on write

![1735802993235](images/OS_flowchart_and_procedures_explained/1735802993235.png)

# Belady Anomaly

![1735803048911](images/OS_flowchart_and_procedures_explained/1735803048911.png)



![1735803079342](images/OS_flowchart_and_procedures_explained/1735803079342.png)



# LRU time-of-use

![1735803131464](images/OS_flowchart_and_procedures_explained/1735803131464.png)

# Page Replacement

![1735803176145](images/OS_flowchart_and_procedures_explained/1735803176145.png)

# Page Buffering

![1735803208059](images/OS_flowchart_and_procedures_explained/1735803208059.png)

# Reclaiming Pages

![1735803275228](images/OS_flowchart_and_procedures_explained/1735803275228.png)

# Thrashing

![1735803302641](images/OS_flowchart_and_procedures_explained/1735803302641.png)
