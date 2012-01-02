jQuery ->
    show_photo = (el) ->
        $el = ($ el)
        for photo in ($ ".post-#{$el.data 'post'}-photo")
            $photo = ($ photo)
            if photo.id == "post-#{$el.data 'post'}-photo-#{$el.data 'photo'}"
                $photo.show()
                prev = $photo.data 'prev'
                next = $photo.data 'next'
            else
                $photo.hide()
        for link in ($ ".post-#{$el.data 'post'}-photo-link")
            if link.id == "post-#{$el.data 'post'}-photo-#{$el.data 'photo'}-link"
                ($ link).addClass 'active'
            else
                ($ link).removeClass 'active'
        $prev_link = ($ "#post-#{$el.data 'post'}-photo-previous-link")
        $next_link = ($ "#post-#{$el.data 'post'}-photo-next-link")
        ($ 'a', $prev_link).data 'photo', prev
        ($ 'a', $next_link).data 'photo', next
        if prev
            $prev_link.removeClass 'disabled'
        else
            $prev_link.addClass 'disabled'
        if next
            $next_link.removeClass 'disabled'
        else
            $next_link.addClass 'disabled'

    ($ '.post-photo-link').click ->
        show_photo this
