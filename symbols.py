# -*- coding: utf-8 -*-

symbol_dict = {u'ä': u'ae', u'æ': u'ae', u'ǽ': u'ae', u'ö': u'oe', u'œ': u'oe', u'ü': u'ue', u'Ä': u'Ae', u'Ö': u'Oe',
               u'À': u'A', u'Á': u'A', u'Â': u'A', u'Ã': u'A', u'Å': u'A', u'Ǻ': u'A', u'Ā': u'A', u'Ă': u'A',
               u'Ą': u'A', u'Ǎ': u'A', u'à': u'a', u'á': u'a', u'â': u'a', u'ã': u'a', u'å': u'a', u'ǻ': u'a',
               u'ā': u'a', u'ă': u'a', u'ą': u'a', u'ǎ': u'a', u'ª': u'a', u'Ç': u'C', u'Ć': u'C', u'Ĉ': u'C',
               u'Ċ': u'C', u'Č': u'C', u'ç': u'c', u'ć': u'c', u'ĉ': u'c', u'ċ': u'c', u'č': u'c', u'Ð': u'D',
               u'Ď': u'D', u'Đ': u'D', u'ð': u'd', u'ď': u'd', u'đ': u'd', u'È': u'E', u'É': u'E', u'Ê': u'E',
               u'Ë': u'E', u'Ē': u'E', u'Ĕ': u'E', u'Ė': u'E', u'Ę': u'E', u'Ě': u'E', u'è': u'e', u'é': u'e',
               u'ê': u'e', u'ë': u'e', u'ē': u'e', u'ĕ': u'e', u'ė': u'e', u'ę': u'e', u'ě': u'e', u'Ĝ': u'G',
               u'Ğ': u'G', u'Ġ': u'G', u'Ģ': u'G', u'Ґ': u'G', u'ĝ': u'g', u'ğ': u'g', u'ġ': u'g', u'ģ': u'g',
               u'ґ': u'g', u'Ĥ': u'H', u'Ħ': u'H', u'ĥ': u'h', u'ħ': u'h', u'І': u'I', u'Ì': u'I', u'Í': u'I',
               u'Î': u'I', u'Ї': u'Yi', u'Ï': u'I', u'Ĩ': u'I', u'Ī': u'I', u'Ĭ': u'I', u'Ǐ': u'I', u'Į': u'I',
               u'İ': u'I', u'і': u'i', u'ì': u'i', u'í': u'i', u'î': u'i', u'ï': u'i', u'ї': u'yi', u'ĩ': u'i',
               u'ī': u'i', u'ĭ': u'i', u'ǐ': u'i', u'į': u'i', u'ı': u'i', u'Ĵ': u'J', u'ĵ': u'j', u'Ķ': u'K',
               u'ķ': u'k', u'Ĺ': u'L', u'Ļ': u'L', u'Ľ': u'L', u'Ŀ': u'L', u'Ł': u'L', u'ĺ': u'l', u'ļ': u'l',
               u'ľ': u'l', u'ŀ': u'l', u'ł': u'l', u'Ñ': u'N', u'Ń': u'N', u'Ņ': u'N', u'Ň': u'N', u'ñ': u'n',
               u'ń': u'n', u'ņ': u'n', u'ň': u'n', u'ŉ': u'n', u'Ò': u'O', u'Ó': u'O', u'Ô': u'O', u'Õ': u'O',
               u'Ō': u'O', u'Ŏ': u'O', u'Ǒ': u'O', u'Ő': u'O', u'Ơ': u'O', u'Ø': u'O', u'Ǿ': u'O', u'ò': u'o',
               u'ó': u'o', u'ô': u'o', u'õ': u'o', u'ō': u'o', u'ŏ': u'o', u'ǒ': u'o', u'ő': u'o', u'ơ': u'o',
               u'ø': u'o', u'ǿ': u'o', u'º': u'o', u'Ŕ': u'R', u'Ŗ': u'R', u'Ř': u'R', u'ŕ': u'r', u'ŗ': u'r',
               u'ř': u'r', u'Ś': u'S', u'Ŝ': u'S', u'Ş': u'S', u'Ș': u'S', u'Š': u'S', u'ẞ': u'SS', u'ś': u's',
               u'ŝ': u's', u'ş': u's', u'ș': u's', u'š': u's', u'ſ': u's', u'Ţ': u'T', u'Ț': u'T', u'Ť': u'T',
               u'Ŧ': u'T', u'ţ': u't', u'ț': u't', u'ť': u't', u'ŧ': u't', u'Ù': u'U', u'Ú': u'U', u'Û': u'U',
               u'Ũ': u'U', u'Ū': u'U', u'Ŭ': u'U', u'Ů': u'U', u'Ű': u'U', u'Ų': u'U', u'Ư': u'U', u'Ǔ': u'U',
               u'Ǖ': u'U', u'Ǘ': u'U', u'Ǚ': u'U', u'Ǜ': u'U', u'Ü': u'Ue', u'ù': u'u', u'ú': u'u', u'û': u'u',
               u'ũ': u'u', u'ū': u'u', u'ŭ': u'u', u'ů': u'u', u'ű': u'u', u'ų': u'u', u'ư': u'u', u'ǔ': u'u',
               u'ǖ': u'u', u'ǘ': u'u', u'ǚ': u'u', u'ǜ': u'u', u'Ý': u'Y', u'Ÿ': u'Y', u'Ŷ': u'Y', u'ý': u'y',
               u'ÿ': u'y', u'ŷ': u'y', u'Ŵ': u'W', u'ŵ': u'w', u'Ź': u'Z', u'Ż': u'Z', u'Ž': u'Z', u'ź': u'z',
               u'ż': u'z', u'ž': u'z', u'Æ': u'AE', u'Ǽ': u'AE', u'ß': u'ss', u'Ĳ': u'IJ', u'ĳ': u'ij', u'Œ': u'OE',
               u'ƒ': u'f', u'Þ': u'TH', u'þ': u'th', u'Є': u'Ye', u'є': u'ye', u'А': u'a', u'Б': u'b', u'В': u'v',
               u'Г': u'g', u'Д': u'd', u'Е': u'e', u'Ё': u'jo', u'Ж': u'zh', u'З': u'z', u'И': u'i', u'Й': u'j',
               u'К': u'k', u'Л': u'l', u'М': u'm', u'Н': u'n', u'О': u'o', u'П': u'p', u'Р': u'r', u'С': u's',
               u'Т': u't', u'У': u'u', u'Ф': u'f', u'Х': u'h', u'Ц': u'c', u'Ч': u'ch', u'Ш': u'sh', u'Щ': u'sch',
               u'Ъ': u'', u'Ы': u'y', u'Ь': u'', u'Э': u'e', u'Ю': u'ju', u'Я': u'ja', u'а': u'a', u'б': u'b',
               u'в': u'v', u'г': u'g', u'д': u'd', u'е': u'e', u'ё': u'jo', u'ж': u'zh', u'з': u'z', u'и': u'i',
               u'й': u'j', u'к': u'k', u'л': u'l', u'м': u'm', u'н': u'n', u'о': u'o', u'п': u'p', u'р': u'r',
               u'с': u's', u'т': u't', u'у': u'u', u'ф': u'f', u'х': u'h', u'ц': u'c', u'ч': u'ch', u'ш': u'sh',
               u'щ': u'sch', u'ъ': u'', u'ы': u'y', u'ь': u'', u'э': u'e', u'ю': u'ju', u'я': u'ja', u'№': u'No',
               u'\u00AD': u'-'}