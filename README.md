# Coding Interview Roadmap – Solutions

A collection of my solutions while following the **Coding Interview Roadmap by DesignGurus.io**.

## Overview

This repository contains my implementations, notes, and explanations for algorithms, data structures, and problem-solving patterns covered in the roadmap.
It aligns with the course’s focus on mastering core concepts through a combination of theory and hands-on coding challenges.

## Purpose

- Strengthen problem-solving skills
- Understand and apply common coding patterns
- Prepare efficiently for technical interviews
- Track personal progress through organized, topic-based solutions

## Directory Layout

<pre><code>
📂 .
├── 📁 01-data-structures-and-algorithms
│   ├── 📁 01-array
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/01-data-structures-and-algorithms/01-array/01.running_sum_of_1d_array.py">01.running_sum_of_1d_array.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/01-data-structures-and-algorithms/01-array/02.contains_duplicate.py">02.contains_duplicate.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/01-data-structures-and-algorithms/01-array/03.left_and_right_sum_differences.py">03.left_and_right_sum_differences.py</a>
│   │   └── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/01-data-structures-and-algorithms/01-array/04.find_the_highest_altitude.py">04.find_the_highest_altitude.py</a>
│   ├── 📁 02-matrix
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/01-data-structures-and-algorithms/02-matrix/01.richest_customer_wealth.py">01.richest_customer_wealth.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/01-data-structures-and-algorithms/02-matrix/02.matrix_diagonal_sum.py">02.matrix_diagonal_sum.py</a>
│   │   └── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/01-data-structures-and-algorithms/02-matrix/03.row_with_maximum_ones.py">03.row_with_maximum_ones.py</a>
│   ├── 📁 03-stack
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/01-data-structures-and-algorithms/03-stack/01.valid_parentheses.py">01.valid_parentheses.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/01-data-structures-and-algorithms/03-stack/02.reverse_string.py">02.reverse_string.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/01-data-structures-and-algorithms/03-stack/03.decimal_to_binary_conversion.py">03.decimal_to_binary_conversion.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/01-data-structures-and-algorithms/03-stack/04.next_greater_element.py">04.next_greater_element.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/01-data-structures-and-algorithms/03-stack/05.sorting_stack.py">05.sorting_stack.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/01-data-structures-and-algorithms/03-stack/06.simplify_path.py">06.simplify_path.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/01-data-structures-and-algorithms/03-stack/07.remove_all_adjacent_duplicates_in_string.py">07.remove_all_adjacent_duplicates_in_string.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/01-data-structures-and-algorithms/03-stack/08.removing_stars_from_a_string.py">08.removing_stars_from_a_string.py</a>
│   │   └── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/01-data-structures-and-algorithms/03-stack/09.make_the_string_great.py">09.make_the_string_great.py</a>
│   ├── 📁 04-queue
│   ├── 📁 05-linked-list
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/01-data-structures-and-algorithms/05-linked-list/01.reverse_linked_list.py">01.reverse_linked_list.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/01-data-structures-and-algorithms/05-linked-list/02.remove_duplicates_from_sorted_list.py">02.remove_duplicates_from_sorted_list.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/01-data-structures-and-algorithms/05-linked-list/03.merge_two_sorted_lists.py">03.merge_two_sorted_lists.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/01-data-structures-and-algorithms/05-linked-list/04.check_doubly_linked_list_characters_palindrome.py">04.check_doubly_linked_list_characters_palindrome.py</a>
│   │   └── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/01-data-structures-and-algorithms/05-linked-list/05.swap_nodes_in_pairs.py">05.swap_nodes_in_pairs.py</a>
│   ├── 📁 06-tree-and-binary-search-tree
│   ├── 📁 07-hash-table
│   ├── 📁 08-hash-set
│   ├── 📁 09-heap
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/01-data-structures-and-algorithms/09-heap/01.take_gifts_from_the_richest_pile.py">01.take_gifts_from_the_richest_pile.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/01-data-structures-and-algorithms/09-heap/02.sort_characters_by_frequency.py">02.sort_characters_by_frequency.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/01-data-structures-and-algorithms/09-heap/03.minimum_cost_to_connect_sticks.py">03.minimum_cost_to_connect_sticks.py</a>
│   │   └── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/01-data-structures-and-algorithms/09-heap/04.find_median_from_data_stream.py">04.find_median_from_data_stream.py</a>
│   ├── 📁 10-graph
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/01-data-structures-and-algorithms/10-graph/01.find_if_path_exists_in_graph.py">01.find_if_path_exists_in_graph.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/01-data-structures-and-algorithms/10-graph/02.number_of_provinces.py">02.number_of_provinces.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/01-data-structures-and-algorithms/10-graph/03.find_eventual_safe_states.py">03.find_eventual_safe_states.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/01-data-structures-and-algorithms/10-graph/04.minimum_number_of_vertices_to_reach_all_nodes.py">04.minimum_number_of_vertices_to_reach_all_nodes.py</a>
│   │   └── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/01-data-structures-and-algorithms/10-graph/05.bus_routes.py">05.bus_routes.py</a>
│   ├── 📁 11-trie
│   ├── 📁 12-sorting
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/01-data-structures-and-algorithms/12-sorting/01.apple_redistribution_into_boxes.py">01.apple_redistribution_into_boxes.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/01-data-structures-and-algorithms/12-sorting/02.sort_array_by_increasing_frequency.py">02.sort_array_by_increasing_frequency.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/01-data-structures-and-algorithms/12-sorting/03.sort_vowels_in_a_string.py">03.sort_vowels_in_a_string.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/01-data-structures-and-algorithms/12-sorting/04.reduction_operations_to_make_the_array_elements_equal.py">04.reduction_operations_to_make_the_array_elements_equal.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/01-data-structures-and-algorithms/12-sorting/05.divide_array_into_arrays_with_max_difference.py">05.divide_array_into_arrays_with_max_difference.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/01-data-structures-and-algorithms/12-sorting/06.top_k_frequent_elements.py">06.top_k_frequent_elements.py</a>
│   │   └── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/01-data-structures-and-algorithms/12-sorting/07.meeting_rooms-ii.py">07.meeting_rooms-ii.py</a>
│   ├── 📁 13-searching
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/01-data-structures-and-algorithms/13-searching/01.maximum_count_of_positive_integer_and_negative_integer.py">01.maximum_count_of_positive_integer_and_negative_integer.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/01-data-structures-and-algorithms/13-searching/02.minimum_common_value.py">02.minimum_common_value.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/01-data-structures-and-algorithms/13-searching/03.frequency_of_the_most_frequent_element.py">03.frequency_of_the_most_frequent_element.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/01-data-structures-and-algorithms/13-searching/04.minimize_the_maximum_of_two_arrays.py">04.minimize_the_maximum_of_two_arrays.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/01-data-structures-and-algorithms/13-searching/05.search_a_2d_matrix_ii.py">05.search_a_2d_matrix_ii.py</a>
│   │   └── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/01-data-structures-and-algorithms/13-searching/06.sqrtx.py">06.sqrtx.py</a>
│   ├── 📁 14-greedy-algorithm
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/01-data-structures-and-algorithms/14-greedy-algorithm/01.valid_palindrome_ii.py">01.valid_palindrome_ii.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/01-data-structures-and-algorithms/14-greedy-algorithm/02.maximum_length_of_pair_chain.py">02.maximum_length_of_pair_chain.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/01-data-structures-and-algorithms/14-greedy-algorithm/03.minimum_add_to_make_parentheses_valid.py">03.minimum_add_to_make_parentheses_valid.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/01-data-structures-and-algorithms/14-greedy-algorithm/04.remove_duplicate_letters.py">04.remove_duplicate_letters.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/01-data-structures-and-algorithms/14-greedy-algorithm/05.largest_palindromic_number.py">05.largest_palindromic_number.py</a>
│   │   └── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/01-data-structures-and-algorithms/14-greedy-algorithm/06.removing_minimum_and_maximum_from_array.py">06.removing_minimum_and_maximum_from_array.py</a>
│   ├── 📁 15-divide-and-conquer
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/01-data-structures-and-algorithms/15-divide-and-conquer/01.longest_nice_substring.py">01.longest_nice_substring.py</a>
│   │   └── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/01-data-structures-and-algorithms/15-divide-and-conquer/02.majority_element.py">02.majority_element.py</a>
├── 📁 02-art-of-recursion
├── 📁 03-common-coding-patterns
│   ├── 📁 01-warm-up
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/01-warm-up/01.contains_duplicate.py">01.contains_duplicate.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/01-warm-up/02.check_if_the_sentence_is_pangram.py">02.check_if_the_sentence_is_pangram.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/01-warm-up/03.reverse_vowels_of_a_string.py">03.reverse_vowels_of_a_string.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/01-warm-up/04.valid_palindrome.py">04.valid_palindrome.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/01-warm-up/05.valid_anagram.py">05.valid_anagram.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/01-warm-up/06.shortest-word-distance.py">06.shortest-word-distance.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/01-warm-up/07.number_of_good_pairs.py">07.number_of_good_pairs.py</a>
│   │   └── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/01-warm-up/08.sqrtx.py">08.sqrtx.py</a>
│   ├── 📁 02-two-pointers
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/02-two-pointers/01.pair_with_target_sum.py">01.pair_with_target_sum.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/02-two-pointers/02.remove_duplicates_from_sorted_array.py">02.remove_duplicates_from_sorted_array.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/02-two-pointers/03.squares_of_a_sorted_array.py">03.squares_of_a_sorted_array.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/02-two-pointers/04.3sum.py">04.3sum.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/02-two-pointers/05.3sum_closest.py">05.3sum_closest.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/02-two-pointers/06.3sum_smaller.py">06.3sum_smaller.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/02-two-pointers/07.sort_colors.py">07.sort_colors.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/02-two-pointers/08.4sum.py">08.4sum.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/02-two-pointers/09.backspace_string_compare.py">09.backspace_string_compare.py</a>
│   │   └── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/02-two-pointers/10.shortest_unsorted_continuous_subarray.py">10.shortest_unsorted_continuous_subarray.py</a>
│   ├── 📁 03-fast-and-slow-pointers
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/03-fast-and-slow-pointers/01.linked_list_cycle.py">01.linked_list_cycle.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/03-fast-and-slow-pointers/02.middle_of_the_linked_list.py">02.middle_of_the_linked_list.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/03-fast-and-slow-pointers/03.linked_list_cycle_ii.py">03.linked_list_cycle_ii.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/03-fast-and-slow-pointers/04.happy_number.py">04.happy_number.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/03-fast-and-slow-pointers/05.palindrome_linked_list.py">05.palindrome_linked_list.py</a>
│   │   └── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/03-fast-and-slow-pointers/06.reorder_list.py">06.reorder_list.py</a>
│   ├── 📁 04-sliding-window
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/04-sliding-window/01.maximum_sum_subarray_of_size_k.py">01.maximum_sum_subarray_of_size_k.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/04-sliding-window/02.minimum_size_subarray_sum.py">02.minimum_size_subarray_sum.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/04-sliding-window/03.longest_substring_with_at_most_k_distinct_characters.py">03.longest_substring_with_at_most_k_distinct_characters.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/04-sliding-window/04.fruit_into_baskets.py">04.fruit_into_baskets.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/04-sliding-window/05.longest_repeating_character_replacement.py">05.longest_repeating_character_replacement.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/04-sliding-window/06.max_consecutive_ones_iii.py">06.max_consecutive_ones_iii.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/04-sliding-window/07.permutation_in_string.py">07.permutation_in_string.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/04-sliding-window/08.find_all_anagrams_in_a_string.py">08.find_all_anagrams_in_a_string.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/04-sliding-window/11.subarray_product_less_than_k.py">11.subarray_product_less_than_k.py</a>
│   │   └── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/04-sliding-window/12.list_of_subarrays_product_less_than_k.py">12.list_of_subarrays_product_less_than_k.py</a>
│   ├── 📁 05-merge-intervals
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/05-merge-intervals/01.merge_intervals.py">01.merge_intervals.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/05-merge-intervals/02.insert_interval.py">02.insert_interval.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/05-merge-intervals/03.interval_list_intersections.py">03.interval_list_intersections.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/05-merge-intervals/04.meeting_room_i.py">04.meeting_room_i.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/05-merge-intervals/05.meeting_rooms_ii.py">05.meeting_rooms_ii.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/05-merge-intervals/06.maximum_cpu_load.py">06.maximum_cpu_load.py</a>
│   │   └── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/05-merge-intervals/07.employee_free_time.py">07.employee_free_time.py</a>
│   ├── 📁 06-cyclic-sort
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/06-cyclic-sort/01.cyclic_sort.py">01.cyclic_sort.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/06-cyclic-sort/02.missing_number.py">02.missing_number.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/06-cyclic-sort/03.find_all_numbers_disappeared_in_an_array.py">03.find_all_numbers_disappeared_in_an_array.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/06-cyclic-sort/04.find_the_duplicate_number.py">04.find_the_duplicate_number.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/06-cyclic-sort/05.find_all_duplicates_in_an_array.py">05.find_all_duplicates_in_an_array.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/06-cyclic-sort/06.find_the_corrupt_one.py">06.find_the_corrupt_one.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/06-cyclic-sort/07.first_missing_positive.py">07.first_missing_positive.py</a>
│   │   └── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/06-cyclic-sort/08.first_k_missing_positive.py">08.first_k_missing_positive.py</a>
│   ├── 📁 07-in-place-reversal-of-linked-list
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/07-in-place-reversal-of-linked-list/01.reverse_linked_list.py">01.reverse_linked_list.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/07-in-place-reversal-of-linked-list/02.reverse_linked_list_ii.py">02.reverse_linked_list_ii.py</a>
│   │   └── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/07-in-place-reversal-of-linked-list/05.rotate_linked_list.py">05.rotate_linked_list.py</a>
│   ├── 📁 08-stack
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/08-stack/01.valid_parentheses.py">01.valid_parentheses.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/08-stack/02.reverse_string.py">02.reverse_string.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/08-stack/03.decimal_to_binary_conversion.py">03.decimal_to_binary_conversion.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/08-stack/04.next_greater_element.py">04.next_greater_element.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/08-stack/05.sorting_stack.py">05.sorting_stack.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/08-stack/06.simplify_path.py">06.simplify_path.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/08-stack/07.remove_all_adjacent_duplicates_in_string.py">07.remove_all_adjacent_duplicates_in_string.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/08-stack/08.removing_stars_from_a_string.py">08.removing_stars_from_a_string.py</a>
│   │   └── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/08-stack/09.make_the_string_great.py">09.make_the_string_great.py</a>
│   ├── 📁 09-monotonic-stack
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/09-monotonic-stack/01.remove_nodes_from_linked_list.py">01.remove_nodes_from_linked_list.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/09-monotonic-stack/02.remove_all_adjacent_duplicates_in_string.py">02.remove_all_adjacent_duplicates_in_string.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/09-monotonic-stack/03.next_greater_element_i.py">03.next_greater_element_i.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/09-monotonic-stack/04.daily_temperatures.py">04.daily_temperatures.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/09-monotonic-stack/05.remove_all_adjacent_duplicates_in_string_ii.py">05.remove_all_adjacent_duplicates_in_string_ii.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/09-monotonic-stack/06.sum_of_subarray_minimums.py">06.sum_of_subarray_minimums.py</a>
│   │   └── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/09-monotonic-stack/07.remove_k_digits.py">07.remove_k_digits.py</a>
│   ├── 📁 10-hash-map
│   ├── 📁 11-level-order-traversal
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/11-level-order-traversal/01.binary_tree_level_order_traversal_ii.py">01.binary_tree_level_order_traversal_ii.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/11-level-order-traversal/02.find_largest_value_in_each_tree_row.py">02.find_largest_value_in_each_tree_row.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/11-level-order-traversal/03.maximum_width_of_binary_tree.py">03.maximum_width_of_binary_tree.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/11-level-order-traversal/04.maximum_level_sum_of_a_binary_tree.py">04.maximum_level_sum_of_a_binary_tree.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/11-level-order-traversal/05.binary_tree_zigzag_level_order_traversal.py">05.binary_tree_zigzag_level_order_traversal.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/11-level-order-traversal/06.even_odd_tree.py">06.even_odd_tree.py</a>
│   │   └── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/11-level-order-traversal/07.n_ary_tree_level_order_traversal.py">07.n_ary_tree_level_order_traversal.py</a>
│   ├── 📁 12-tree-breadth-first-search
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/12-tree-breadth-first-search/01.binary_tree_level_order_traversal.py">01.binary_tree_level_order_traversal.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/12-tree-breadth-first-search/02.binary_tree_level_order_traversal_ii.py">02.binary_tree_level_order_traversal_ii.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/12-tree-breadth-first-search/03.binary_tree_zigzag_level_order_traversal.py">03.binary_tree_zigzag_level_order_traversal.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/12-tree-breadth-first-search/04.average_of_levels_in_binary_tree.py">04.average_of_levels_in_binary_tree.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/12-tree-breadth-first-search/05.minimum_depth_of_binary_tree.py">05.minimum_depth_of_binary_tree.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/12-tree-breadth-first-search/06.level_order_successor.py">06.level_order_successor.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/12-tree-breadth-first-search/07.populating_next_right_pointers_in_each_node.py">07.populating_next_right_pointers_in_each_node.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/12-tree-breadth-first-search/08.connect_all_level_order_siblings.py">08.connect_all_level_order_siblings.py</a>
│   │   └── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/12-tree-breadth-first-search/09.binary_tree_right_side_view.py">09.binary_tree_right_side_view.py</a>
│   ├── 📁 13-tree-depth-first-search
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/13-tree-depth-first-search/01.path_sum.py">01.path_sum.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/13-tree-depth-first-search/02.path_sum_ii.py">02.path_sum_ii.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/13-tree-depth-first-search/03.sum_root_to_leaf_numbers.py">03.sum_root_to_leaf_numbers.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/13-tree-depth-first-search/04.check_if_a_string_is_a_valid_sequence_from_root_to_leaves_path.py">04.check_if_a_string_is_a_valid_sequence_from_root_to_leaves_path.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/13-tree-depth-first-search/05.path_sum_iii.py">05.path_sum_iii.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/13-tree-depth-first-search/06.diameter_of_binary_tree.py">06.diameter_of_binary_tree.py</a>
│   │   └── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/13-tree-depth-first-search/07.binary_tree_maximum_path_sum.py">07.binary_tree_maximum_path_sum.py</a>
│   ├── 📁 14-graph
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/14-graph/01.find_if_path_exists_in_graph.py">01.find_if_path_exists_in_graph.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/14-graph/02.number_of_provinces.py">02.number_of_provinces.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/14-graph/03.find_eventual_safe_states.py">03.find_eventual_safe_states.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/14-graph/04.minimum_number_of_vertices_to_reach_all_nodes.py">04.minimum_number_of_vertices_to_reach_all_nodes.py</a>
│   │   └── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/14-graph/05.bus_routes.py">05.bus_routes.py</a>
│   ├── 📁 15-island-matrix-traversal
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/15-island-matrix-traversal/01.number_of_islands.py">01.number_of_islands.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/15-island-matrix-traversal/02.max_area_of_island.py">02.max_area_of_island.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/15-island-matrix-traversal/03.flood_fill.py">03.flood_fill.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/15-island-matrix-traversal/04.number_of_closed_islands.py">04.number_of_closed_islands.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/15-island-matrix-traversal/05.island_perimeter.py">05.island_perimeter.py</a>
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/15-island-matrix-traversal/06.number_of_distinct_islands.py">06.number_of_distinct_islands.py</a>
│   │   └── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/15-island-matrix-traversal/07.detect_cycles_in_2d_grid.py">07.detect_cycles_in_2d_grid.py</a>
│   ├── 📁 16-two-heaps
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/16-two-heaps/01.find_median_from_data_stream.py">01.find_median_from_data_stream.py</a>
│   │   └── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/16-two-heaps/04.find_right_interval.py">04.find_right_interval.py</a>
│   ├── 📁 17-subset
│   │   ├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/17-subset/78.subsets.py">78.subsets.py</a>
│   │   └── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/03-common-coding-patterns/17-subset/90.subsets_ii.py">90.subsets_ii.py</a>
│   ├── 📁 18-modified-binary-search
│   ├── 📁 19-bitwise-xor
│   ├── 📁 20-top-k-elements
│   ├── 📁 21-k-way-merge
│   ├── 📁 22-greedy-algorithm
│   ├── 📁 23-dp-0-or-1-knapsack
│   ├── 📁 24-dp-fibonacci-number
│   ├── 📁 25-dp-palindromic-subsequence
│   ├── 📁 26-backtracking
│   ├── 📁 27-trie
│   ├── 📁 28-graph-topological-sort
│   ├── 📁 29-union-find
│   ├── 📁 30-ordered-set
│   ├── 📁 31-prefix-sum
│   ├── 📁 32-multi-threading
├── 📁 04-advanced-coding-patterns
├── 📁 05-dynamic-programming
│   ├── 📁 01-0-or-1-knapsack
│   ├── 📁 02-unbounded-knapsack
│   ├── 📁 03-fibonacci-numbers
│   ├── 📁 04-palindromic-subsequence
│   ├── 📁 05-longest-common-substring
├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/LICENSE">LICENSE</a>
├── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/README.md">README.md</a>
└── <a href="https://github.com/abdulaziz7225/coding-interview-roadmap/blob/main/directory_layout_script.py">directory_layout_script.py</a>
</code></pre>
