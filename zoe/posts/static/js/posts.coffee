jQuery ->
    show_photo = (el) ->
        $el = ($ el)
        return unless $el.hasClass 'post-photo-link'
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
            ($ 'a', $prev_link).addClass 'post-photo-link'
        else
            $prev_link.addClass 'disabled'
            ($ 'a', $prev_link).removeClass 'post-photo-link'
        if next
            $next_link.removeClass 'disabled'
            ($ 'a', $next_link).addClass 'post-photo-link'
        else
            $next_link.addClass 'disabled'
            ($ 'a', $next_link).removeClass 'post-photo-link'

    ($ '.post-photo-link').click ->
        show_photo this
