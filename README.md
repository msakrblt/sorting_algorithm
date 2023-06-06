# Sorting Algorithms

# 1-Selection Sort: O(N^2)
Her bir iterasyon için ${i}. sayı ile en küçük sayının indexlerinin yeri değiştirilir.

# 2-Insertion Sort: O(N^2) - Best Case: O(n)
Sıralı ayracı mevcuttur ve sol tarafındaki sayılar sıralıdır. Sıralı ayracı ilk sayının sağında başlar ve her bir adımdan sonra bir ileri taşınarak ayracın sol tarafını sıralı hale getirir.

# 3-Bubble Sort: O(N^2)
Her bir iterasyonda ilk iki elemandan başlayarak dizinin sonuna kadar, iki sayıyı karşılaştırıp yer değişikliği yapan ve bu adımları tekrar eden yapıdır. Her bir iterasyonun sonunda en büyük sayı sona taşınır.

# 4-Counting Sort: O(N)
Sırasız dizideki elemanların kaç defa geçtiğini ikinci bir dizide tutup sonrasında bu diziyi ekrana yazdıran sıralama algoritmasıdır.
Lineer çalışma zamanına sahiptir. Hafıza karmaşıklığı açısından sıkıntı doğurabilir. Örneğin, arr=[1,2,10000] olduğu durumda 10000 elemanlı yeni bir dizi oluşturur ve sadece 3 elemanı dolu olacaktır.
